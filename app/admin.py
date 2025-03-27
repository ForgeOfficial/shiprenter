from django.contrib import admin
from django.utils.html import format_html

from app.models.Category import Category
from app.models.Rental import Rental
from app.models.Ship import Ship
from app.models.Size import Size


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_ships_count')
    search_fields = ('name',)

    def get_ships_count(self, obj):
        return obj.ships.count()

    get_ships_count.short_description = 'Nombre de navires'

@admin.register(Size)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_ships_count')
    search_fields = ('name',)

    def get_ships_count(self, obj):
        return obj.ships.count()

    get_ships_count.short_description = 'Nombre de navires'


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'size', 'price', 'get_image_preview')
    list_filter = ('category', 'size')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'get_image_preview')
    fieldsets = (
        ('Informations de base', {
            'fields': ('name', 'category', 'size','crew')
        }),
        ('Détails financiers', {
            'fields': ('price',)
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Médias', {
            'fields': ('image', 'get_image_preview')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image)
        return 'Aucune image'

    get_image_preview.short_description = 'Aperçu'


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ship', 'duration', 'created_at', 'display_total_price')

    list_filter = ('created_at', 'duration')

    search_fields = ('user__username', 'user__email', 'ship__name')

    readonly_fields = ('created_at', 'display_total_price')

    fieldsets = (
        ('Informations de location', {
            'fields': ('user', 'ship', 'duration')
        }),
        ('Détails financiers', {
            'fields': ('display_total_price',)
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def display_total_price(self, obj):
        return f"{obj.total_price()} €"

    display_total_price.short_description = 'Prix total'

    actions = ['extend_duration']

    def extend_duration(self, request, queryset):
        for rental in queryset:
            rental.duration += 1
            rental.save()

        count = queryset.count()
        if count == 1:
            message = "1 location a été prolongée d'un jour."
        else:
            message = f"{count} locations ont été prolongées d'un jour."
        self.message_user(request, message)

    extend_duration.short_description = "Prolonger la location d'un jour"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user', 'ship')
        return queryset