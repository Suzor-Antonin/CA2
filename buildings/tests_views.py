from django.test import TestCase
from .models import Building
from django.urls import reverse


class ViewsWorkTests(TestCase):

    # positive tests
    def test_actual_views(self):
        """Test whether the accessible views do return a 200 code,
        which means you can find them and visit them."""
        response = self.client.get(reverse('buildings:home'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:sort-by-pk'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:sort-by-address'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:sort-by-name'))
        self.assertEqual(response.status_code, 200)

        # We need to create a dummy Building to test the CRUD views
        Building.objects.create(pk=40)

        response = self.client.get(reverse('buildings:create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:read', kwargs={'pk': 40}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:update', kwargs={'pk': 40}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('buildings:delete', kwargs={'pk': 40}))
        self.assertEqual(response.status_code, 200)

    # positive tests
    def test_redirect_views(self):
        """Test whether the redirect views do return a 302 code,
        which means that when you stumble on them, you are redirected to an actual view."""
        response = self.client.get(reverse('buildings:sort-by'))
        self.assertEqual(response.status_code, 302)


class SortViewsTests(TestCase):

    # negative tests
    def test_no_data(self):
        """Test whether the correct message is displayed when no data is available."""
        response = self.client.get(reverse('buildings:sort-by-pk'))
        self.assertContains(response, '<p>No buildings registered yet.</p>')

        response = self.client.get(reverse('buildings:sort-by-name'))
        self.assertContains(response, '<p>No buildings registered yet.</p>')

        response = self.client.get(reverse('buildings:sort-by-address'))
        self.assertContains(response, '<p>No buildings registered yet.</p>')

    # positive tests
    def test_correct_pk_sort(self):
        """Test whether the sorting by negative primary key works as intended."""
        building1 = Building.objects.create(pk=88)
        building2 = Building.objects.create(pk=87)
        response = self.client.get(reverse('buildings:sort-by-pk'))
        self.assertQuerysetEqual(response.context['building_list'], [building1, building2])

    # positive tests
    def test_correct_name_sort(self):
        """Test whether the sorting by building name works as intended."""
        building1 = Building.objects.create(name='First building')
        building2 = Building.objects.create(name='Second building')
        response = self.client.get(reverse('buildings:sort-by-name'))
        self.assertQuerysetEqual(response.context['building_list'], [building1, building2])

    # positive tests
    def test_correct_address_sort(self):
        """Test whether the sorting by address works as intended."""
        building11 = Building.objects.create(country='France', street='Avenue de la République')
        building12 = Building.objects.create(country='France', street='Rue Voltaire')
        building21 = Building.objects.create(country='Ireland', city='Cork')
        building22 = Building.objects.create(country='Ireland', city='Dublin')
        response = self.client.get(reverse('buildings:sort-by-address'))
        self.assertQuerysetEqual(response.context['building_list'], [building11, building12, building21, building22])
