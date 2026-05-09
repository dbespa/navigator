from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from traffic.forms import LocationForm, RoadSegmentForm, CongestionTypeForm, TrafficForm
from traffic.models import Location, RoadSegment, CongestionType, Traffic


def home(request):
    return render(request, 'traffic/home.html')


def location_handler(request, pk=None):
    if request.path.endswith('/update/') and pk:
        location = get_object_or_404(Location, pk=pk)

        if request.method == 'POST':
            form = LocationForm(request.POST, instance=location)
            if form.is_valid():
                form.save()
                return redirect('location_detail', pk=location.pk)
            else:
                return render(request, 'traffic/create_location.html', {
                    'form': form,
                    'location': location,
                    'error': 'Форма была неверной'
                })
        else:
            form = LocationForm(instance=location)
            return render(request, 'traffic/create_location.html', {
                'form': form,
                'location': location
            })

    elif request.path.endswith('/delete/') and pk:
        location = get_object_or_404(Location, pk=pk)

        if request.method == 'POST':
            location.delete()
            return redirect('locations')
        else:
            return render(request, 'traffic/delete.html', {
                'object': location,
                'type': 'Location',
                'cancel_url': 'location_detail',
                'cancel_id': location.id
            })

    elif request.path.endswith('/create/'):
        if request.method == 'POST':
            form = LocationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('locations')
            else:
                return render(request, 'traffic/create_location.html', {
                    'form': form,
                    'error': 'Форма была неверной'
                })
        else:
            form = LocationForm()
            return render(request, 'traffic/create_location.html', {'form': form})

    elif request.method == 'GET':
        if pk is None:
            if request.GET.get('format') == 'json' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                locations = Location.objects.all().values()
                return JsonResponse(list(locations), safe=False)
            else:
                locations = Location.objects.all().order_by('name')
                return render(request, 'traffic/list_locations.html', {'locations': locations})
        else:
            location = get_object_or_404(Location, pk=pk)
            return render(request, 'traffic/detail_location.html', {'location': location})

    elif request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations')
        else:
            return render(request, 'traffic/create_location.html', {'form': form, 'error': 'Форма была неверной'})


def road_handler(request, pk=None):
    if request.path.endswith('/update/') and pk:
        road = get_object_or_404(RoadSegment, pk=pk)

        if request.method == 'POST':
            form = RoadSegmentForm(request.POST, instance=road)
            if form.is_valid():
                form.save()
                return redirect('road_detail', pk=road.pk)
            else:
                return render(request, 'traffic/create_road.html', {
                    'form': form,
                    'road': road,
                    'error': 'Форма была неверной'
                })
        else:
            form = RoadSegmentForm(instance=road)
            return render(request, 'traffic/create_road.html', {
                'form': form,
                'road': road
            })

    elif request.path.endswith('/delete/') and pk:
        road = get_object_or_404(RoadSegment, pk=pk)

        if request.method == 'POST':
            road.delete()
            return redirect('roads')
        else:
            return render(request, 'traffic/delete.html', {
                'object': road,
                'type': 'RoadSegment',
                'cancel_url': 'road_detail',
                'cancel_id': road.id
            })

    elif request.path.endswith('/create/'):
        if request.method == 'POST':
            form = RoadSegmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('roads')
            else:
                return render(request, 'traffic/create_road.html', {
                    'form': form,
                    'error': 'Форма была неверной'
                })
        else:
            form = RoadSegmentForm()
            return render(request, 'traffic/create_road.html', {'form': form})

    elif request.method == 'GET':
        if pk is None:
            if request.GET.get('format') == 'json' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                roads = RoadSegment.objects.all().values()
                return JsonResponse(list(roads), safe=False)
            else:
                roads = RoadSegment.objects.all()
                return render(request, 'traffic/list_roads.html', {'roads': roads})
        else:
            road = get_object_or_404(RoadSegment, pk=pk)
            return render(request, 'traffic/detail_road.html', {'road': road})

    elif request.method == 'POST':
        form = RoadSegmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roads')
        else:
            return render(request, 'traffic/create_road.html', {'form': form, 'error': 'Форма была неверной'})


def contype_handler(request, pk=None):
    if request.path.endswith('/update/') and pk:
        contype = get_object_or_404(CongestionType, pk=pk)

        if request.method == 'POST':
            form = CongestionTypeForm(request.POST, instance=contype)
            if form.is_valid():
                form.save()
                return redirect('contype_detail', pk=contype.pk)
            else:
                return render(request, 'traffic/create_contype.html', {
                    'form': form,
                    'contype': contype,
                    'error': 'Форма была неверной'
                })
        else:
            form = CongestionTypeForm(instance=contype)
            return render(request, 'traffic/create_contype.html', {
                'form': form,
                'contype': contype
            })

    elif request.path.endswith('/delete/') and pk:
        contype = get_object_or_404(CongestionType, pk=pk)

        if request.method == 'POST':
            contype.delete()
            return redirect('contypes')
        else:
            return render(request, 'traffic/delete.html', {
                'object': contype,
                'type': 'CongestionType',
                'cancel_url': 'contype_detail',
                'cancel_id': contype.id
            })

    elif request.path.endswith('/create/'):
        if request.method == 'POST':
            form = CongestionTypeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('contypes')
            else:
                return render(request, 'traffic/create_contype.html', {
                    'form': form,
                    'error': 'Форма была неверной'
                })
        else:
            form = CongestionTypeForm()
            return render(request, 'traffic/create_contype.html', {'form': form})

    elif request.method == 'GET':
        if pk is None:
            if request.GET.get('format') == 'json' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                contypes = CongestionType.objects.all().values()
                return JsonResponse(list(contypes), safe=False)
            else:
                contypes = CongestionType.objects.all()
                return render(request, 'traffic/list_contypes.html', {'contypes': contypes})
        else:
            contype = get_object_or_404(CongestionType, pk=pk)
            return render(request, 'traffic/detail_contype.html', {'contype': contype})

    elif request.method == 'POST':
        form = CongestionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contypes')
        else:
            return render(request, 'traffic/create_contype.html', {'form': form, 'error': 'Форма была неверной'})


def traffic_handler(request, pk=None):
    if request.path.endswith('/update/') and pk:
        traffic = get_object_or_404(Traffic, pk=pk)

        if request.method == 'POST':
            form = TrafficForm(request.POST, instance=traffic)
            if form.is_valid():
                form.save()
                return redirect('traffic_detail', pk=traffic.pk)
            else:
                return render(request, 'traffic/create_traffic.html', {
                    'form': form,
                    'traffic': traffic,
                    'error': 'Форма была неверной'
                })
        else:
            form = TrafficForm(instance=traffic)
            return render(request, 'traffic/create_traffic.html', {
                'form': form,
                'traffic': traffic
            })

    elif request.path.endswith('/delete/') and pk:
        traffic = get_object_or_404(Traffic, pk=pk)

        if request.method == 'POST':
            traffic.delete()
            return redirect('traffic')
        else:
            return render(request, 'traffic/delete.html', {
                'object': traffic,
                'type': 'Traffic',
                'cancel_url': 'traffic_detail',
                'cancel_id': traffic.id
            })

    elif request.path.endswith('/create/'):
        if request.method == 'POST':
            form = TrafficForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('traffic')
            else:
                return render(request, 'traffic/create_traffic.html', {
                    'form': form,
                    'error': 'Форма была неверной'
                })
        else:
            form = TrafficForm()
            return render(request, 'traffic/create_traffic.html', {'form': form})

    elif request.method == 'GET':
        if pk is None:
            if request.GET.get('format') == 'json' or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                traffics = Traffic.objects.all().values()
                return JsonResponse(list(traffics), safe=False)
            else:
                traffics = Traffic.objects.all().select_related('road_segment', 'congestion_type')
                return render(request, 'traffic/list_traffic.html', {'traffics': traffics})
        else:
            traffic = get_object_or_404(Traffic.objects.select_related('road_segment', 'congestion_type'), pk=pk)
            return render(request, 'traffic/detail_traffic.html', {'traffic': traffic})

    elif request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traffic')
        else:
            return render(request, 'traffic/create_traffic.html', {'form': form, 'error': 'Форма была неверной'})

# def list_locations(request):
#     locations = Location.objects.all().order_by('name')
#     return render(request, 'traffic/list_locations.html', {'locations': locations})
#
# def list_roads(request):
#     roads = RoadSegment.objects.all()
#     return render(request, 'traffic/list_roads.html', {'roads': roads})
#
# def roads(request):
#     if request.method == 'GET':
#         return list_roads(request)
#     elif request.method == 'POST':
#         pass
#
# def list_contypes(request):
#     contypes = CongestionType.objects.all()
#     return render(request, 'traffic/list_contypes.html', {'contypes': contypes})
#
# def list_traffic(request):
#     traffics = RoadSegment.objects.all()
#     return render(request, 'traffic/list_traffic.html', {'traffics': traffics})
#
# # @ensure_csrf_cookie
# def get_locations(request):
#     locations = Location.objects.all().values()
#     return JsonResponse(list(locations), safe=False)
#
# @csrf_exempt
# def get_roads(request):
#     print(request.method)
#     roads = RoadSegment.objects.all().values()
#     return JsonResponse(list(roads), safe=False)
#
# # @ensure_csrf_cookie
# def get_congestion_types(request):
#     congestion_types = CongestionType.objects.all().values()
#     return JsonResponse(list(congestion_types), safe=False)
#
# # @ensure_csrf_cookie
# def get_traffic(request):
#     traffic = Traffic.objects.all().values()
#     return JsonResponse(list(traffic), safe=False)
#
# def create_location(request):
#     error = ''
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error='Форма была неверной'
#     form = LocationForm()
#     data = {
#         'form': form,
#     }
#     return render(request, 'traffic/create_location.html', data)
#
# def create_road(request):
#     error = ''
#     if request.method == 'POST':
#         form = RoadSegmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Форма была неверной'
#     form = RoadSegmentForm()
#     data = {
#         'form': form,
#     }
#     return render(request, 'traffic/create_road.html', data)
#
# def create_contype(request):
#     error = ''
#     if request.method == 'POST':
#         form = CongestionTypeForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'Форма была неверной'
#     form = CongestionTypeForm()
#     data = {
#         'form': form,
#     }
#     return render(request, 'traffic/create_contype.html', data)
#
# class LocationDetailView(DetailView):
#     model = Location
#     template_name = 'traffic/detail_location.html'
#     context_object_name = 'location'
#
# class RoadDetailView(DetailView):
#     model = RoadSegment
#     template_name = 'traffic/detail_road.html'
#     context_object_name = 'road'
#
# class ContypeDetailView(DetailView):
#     model = CongestionType
#     template_name = 'traffic/detail_contype.html'
#     context_object_name = 'contype'
#
# class TrafficDetailView(DetailView):
#     model = Traffic
#     template_name = 'traffic/detail_traffic.html'
#     context_object_name = 'traffic'
#
# class LocationUpdateView(UpdateView):
#     model = Location
#     template_name = 'traffic/create_location.html'
#     form_class = LocationForm
#
# class RoadUpdateView(UpdateView):
#     model = RoadSegment
#     template_name = 'traffic/create_road.html'
#     form_class = RoadSegmentForm
#
# class ContypeUpdateView(UpdateView):
#     model = CongestionType
#     template_name = 'traffic/create_contype.html'
#     form_class = CongestionTypeForm
#
# class TrafficUpdateView(UpdateView):
#     model = Traffic
#     template_name = 'traffic/create_location.html'
#     form_class = TrafficForm
#
# class LocationDeleteView(DeleteView):
#     model = Location
#     success_url = '/locations'
#     template_name = 'traffic/delete.html'
#
# class RoadDeleteView(DeleteView):
#     model = RoadSegment
#     success_url = '/roads'
#     template_name = 'traffic/delete.html'
#
# class ContypeDeleteView(DeleteView):
#     model = CongestionType
#     success_url = '/contypes'
#     template_name = 'traffic/delete.html'
