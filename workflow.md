
# Django Request–Response Architecture

The following diagram illustrates how a request travels through Django from the browser to the database and back to the user.

---

## Django Architecture

```text
                                        HTTP Request
+--------+        Request        +-------------+        Request
|  User  | --------------------> | Web Server  | --------------------+
+--------+ <-------------------- +-------------+ <--------------------+
          HTTP Response                ^
                                       |
                                       |
                                       v
                               +----------------+
                               |     Django     |
                               +----------------+
                                       |
                                       v
                              +------------------+
                              |   URL Resolver   |
                              +------------------+
                                       |
                                       v
                               +---------------+
                               | project/urls.py |
                               +---------------+
                                       |
                           include("app.urls")
                                       |
                                       v
                               +---------------+
                               |   app/urls.py |
                               +---------------+
                                       |
                                       v
                               +---------------+
                               |   views.py    |
                               +---------------+
                                 |           |
                   Database      |           | Render
                    Access       |           | Template
                                 |           |
                                 v           v
                           +-------------+   +-------------+
                           |  models.py  |   | Templates/  |
                           +-------------+   +-------------+
                                 |
                                 |
                                 v
                           +-------------+
                           |  Database   |
                           +-------------+
                                 |
                                 +------------------+
                                                    |
                                                    v
                                            +----------------+
                                            | HttpResponse   |
                                            +----------------+
                                                    |
                                                    |
                                                    v
                                                +--------+
                                                |  User  |
                                                +--------+
```

---

# Step-by-Step Flow

## 1. User

The user opens a website or enters a URL.

Example:

```
http://127.0.0.1:8000/
```

The browser sends an **HTTP Request**.

↓

## 2. Web Server

The web server receives the request.

During development, Django's built-in development server acts as the web server.

```bash
python manage.py runserver
```

or

```bash
uv run manage.py runserver
```

↓

## 3. Django

Django receives the request from the web server.

Its job is to determine which part of the application should handle the request.

↓

## 4. URL Resolver

The URL Resolver matches the requested URL with the URL patterns defined in the project.

↓

## 5. `project/urls.py`

The root URL configuration is checked first.

Example:

```python
urlpatterns = [
    path("", include("home.urls")),
]
```

If the request belongs to an application, Django forwards it to that application's `urls.py`.

↓

## 6. `app/urls.py`

Application-level URL patterns determine which view should execute.

Example:

```python
urlpatterns = [
    path("", views.home),
    path("about/", views.about),
]
```

↓

## 7. `views.py`

The view contains the business logic.

Example:

```python
def home(request):
    return render(request, "index.html")
```

The view decides whether it needs to access the database.

---

### If Database Access is Required

```
views.py
     │
     ▼
models.py
     │
     ▼
Database
```

The model communicates with the database using Django ORM.

Example:

```python
products = Product.objects.all()
```

The data is returned back to the view.

---

### If HTML Needs to be Generated

The view renders a template.

```python
return render(request, "index.html", context)
```

```
views.py
     │
     ▼
Templates
```

Templates combine:

- HTML
- CSS
- JavaScript
- Django Template Language (DTL)
- Context data

to generate the final HTML page.

---

## 8. HttpResponse

After processing, the view returns an HTTP Response.

Examples:

```python
return HttpResponse("Hello Django")
```

```python
return render(request, "index.html")
```

```python
return JsonResponse(data)
```

↓

## 9. Web Server

The response is sent back through the web server.

↓

## 10. User

The browser receives the response and displays the webpage.

---

# Complete Flow

```text
User
 │
 ▼
Web Server
 │
 ▼
Django
 │
 ▼
URL Resolver
 │
 ▼
project/urls.py
 │
 ▼
app/urls.py
 │
 ▼
views.py
 │
 ├────────────► models.py
 │                  │
 │                  ▼
 │              Database
 │                  │
 │◄─────────────────┘
 │
 └────────────► Templates
                    │
                    ▼
              HttpResponse
                    │
                    ▼
               Web Server
                    │
                    ▼
                  User
```

---

# Responsibilities of Each Component

| Component                 | Responsibility                                |
| ------------------------- | --------------------------------------------- |
| **User**            | Sends an HTTP request through the browser     |
| **Web Server**      | Receives requests and forwards them to Django |
| **Django**          | Processes incoming requests                   |
| **URL Resolver**    | Matches the requested URL                     |
| **project/urls.py** | Root URL routing                              |
| **app/urls.py**     | Application-specific URL routing              |
| **views.py**        | Contains business logic                       |
| **models.py**       | Interacts with the database using Django ORM  |
| **Database**        | Stores and retrieves application data         |
| **Templates**       | Generates dynamic HTML pages                  |
| **HttpResponse**    | Sends the final response back to the browser  |

---

# Request Lifecycle Summary

```text
User
   │
   ▼
Web Server
   │
   ▼
Django
   │
   ▼
URL Resolver
   │
   ▼
project/urls.py
   │
   ▼
app/urls.py
   │
   ▼
views.py
   ├──► models.py ───► Database
   └──► Templates
            │
            ▼
      HttpResponse
            │
            ▼
      Web Server
            │
            ▼
           User
```
