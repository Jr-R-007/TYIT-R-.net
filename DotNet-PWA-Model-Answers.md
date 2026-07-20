# .NET Core and PWA - MODEL ANSWERS (30 Marks, 1 Hour)

**Total Time: 60 minutes | Marks: 30 | Format: Choose 3 from each module**

---

## MODULE 1: COMPLETE ANSWERS (Choose 3 out of 5)

---

### Q1: .NET Ecosystem Architecture (5 marks) ⏱️ 12 minutes

#### **a) Differentiate .NET Framework vs .NET Core/.NET 5+ (3 marks)**

| Aspect | .NET Framework | .NET Core/.NET 5+ |
|--------|---|---|
| **Platform** | Windows only | Cross-platform (Windows, Linux, macOS) |
| **Open Source** | Proprietary | Open-source (MIT License) |
| **Performance** | Slower | ~2-3x faster |
| **Deployment** | Full .NET runtime required | Self-contained deployment |
| **Version Release** | Slower (2-3 years) | Annual releases |
| **Modern Features** | Limited updates | Regular updates, async/await, LINQ |
| **Use Case** | Legacy enterprise apps | Cloud, microservices, containers |

**Advantages of .NET Core:**
- **Example 1:** Deploy same app on Windows server, Linux container, and macOS without modification
- **Example 2:** Build containerized microservices with Docker, deploy to Kubernetes

---

#### **b) Common Language Runtime (CLR) - 2 marks**

**Definition:** CLR is the runtime environment that executes .NET applications.

**Role in executing C# code:**
1. **Compilation:** C# code → IL (Intermediate Language) during compilation
2. **JIT Compilation:** IL → Native machine code at runtime via JIT compiler
3. **Memory Management:** Automatic garbage collection
4. **Type Safety:** Enforces type checking, array bounds checking
5. **Exception Handling:** Manages try-catch-finally execution

```
C# Code → Compiler → IL Code → CLR → JIT → Native Machine Code → Execution
```

---

### Q2: C# Language Fundamentals and Control Structures (5 marks) ⏱️ 13 minutes

#### **a) C# Program with Data Types (2 marks)**

```csharp
using System;

class Program
{
    static void Main()
    {
        // Different data types
        int age = 25;                          // Integer
        string name = "Rupesh";                // String
        float salary = 50000.50f;              // Float (single precision)
        bool isActive = true;                  // Boolean
        decimal accountBalance = 100000.75m;   // Decimal (high precision)

        // Operations
        int nextYear = age + 1;                // Arithmetic
        string fullInfo = name + " is " + age; // String concatenation
        decimal bonus = accountBalance * 0.10m; // Decimal operation
        
        Console.WriteLine($"Name: {name}");
        Console.WriteLine($"Age: {age}, Next Year: {nextYear}");
        Console.WriteLine($"Salary: {salary}");
        Console.WriteLine($"Account: {accountBalance}, Bonus: {bonus}");
        Console.WriteLine($"Status: {isActive}");
    }
}
```

**Output:**
```
Name: Rupesh
Age: 25, Next Year: 26
Salary: 50000.5
Account: 100000.75, Bonus: 10000.0750
Status: True
```

---

#### **b) If-else vs Switch vs Ternary Operator (3 marks)**

**If-Else:**
```csharp
int marks = 85;
if (marks >= 90)
    Console.WriteLine("A");
else if (marks >= 80)
    Console.WriteLine("B");
else if (marks >= 70)
    Console.WriteLine("C");
else
    Console.WriteLine("F");
```

**Switch Statement:**
```csharp
switch (marks / 10)
{
    case 10:
    case 9:
        Console.WriteLine("A");
        break;
    case 8:
        Console.WriteLine("B");
        break;
    case 7:
        Console.WriteLine("C");
        break;
    default:
        Console.WriteLine("F");
        break;
}
```

**Ternary Operator:**
```csharp
string grade = marks >= 90 ? "A" : marks >= 80 ? "B" : marks >= 70 ? "C" : "F";
Console.WriteLine(grade);
```

**Preference for Multiple Conditions:**
- **Ternary:** 2 conditions max (readability)
- **If-Else:** 3+ conditions, complex logic ✅ **BEST**
- **Switch:** Fixed values, limited conditions

**Answer:** Use **If-Else** for multiple conditions as it's more readable and maintainable.

---

### Q3: Object-Oriented Programming Principles (5 marks) ⏱️ 12 minutes

#### **a) Inheritance and Polymorphism (3 marks)**

**Inheritance - Single Level:**
```csharp
// Base class
public class Animal
{
    public virtual void Speak()
    {
        Console.WriteLine("Animal makes a sound");
    }
}

// Derived class
public class Dog : Animal
{
    public override void Speak()  // Method overriding
    {
        Console.WriteLine("Dog barks: Woof Woof!");
    }
}

// Polymorphic behavior
Animal animal = new Dog();  // Reference of base, object of derived
animal.Speak();            // Outputs: "Dog barks: Woof Woof!"
```

**Polymorphism Example:**
```csharp
Animal dog = new Dog();
Animal cat = new Cat();
dog.Speak();  // Dog barks
cat.Speak();  // Cat meows
// Same method call, different behavior = Polymorphism
```

---

#### **b) Interfaces vs Abstract Classes (2 marks)**

| Feature | Interface | Abstract Class |
|---------|-----------|---|
| **Implementation** | No method body | Can have method bodies |
| **Multiple** | Multiple inheritance | Single inheritance |
| **Variables** | No instance variables | Can have state |
| **Access Modifier** | Public only | Can be private, protected |
| **Use Case** | Contract/capability | Common functionality |

**Practical Example:**
```csharp
// Interface - defines contract
public interface IPayable
{
    void Pay(decimal amount);
}

// Abstract class - provides base implementation
public abstract class Employee
{
    public abstract void Work();
    public void TakeBreak() { Console.WriteLine("On break"); }
}

// Implementation
public class Manager : Employee, IPayable
{
    public override void Work() { Console.WriteLine("Managing team"); }
    public void Pay(decimal amount) { Console.WriteLine($"Paid: {amount}"); }
}
```

---

### Q4: ASP.NET Core Web Fundamentals (5 marks) ⏱️ 12 minutes

#### **a) ASP.NET Core Request Lifecycle (3 marks)**

```
HTTP Request
    ↓
[Middleware Pipeline]
    ↓
1. Routing Middleware → Route to Controller
    ↓
2. Authentication Middleware → Verify user
    ↓
3. Authorization Middleware → Check permissions
    ↓
4. Controller Action → Execute business logic
    ↓
5. View Rendering/Response Generation
    ↓
[Middleware Pipeline - Reverse]
    ↓
HTTP Response ← Sent to client
```

**Key Points:**
- Middleware: Pre-processing and post-processing hooks
- Each middleware can short-circuit the pipeline
- Routing directs request to correct controller
- Response flows back through middleware

---

#### **b) MVC vs Razor Pages (2 marks)**

| Aspect | MVC | Razor Pages |
|--------|-----|---|
| **Structure** | Separate Controllers & Views | Pages folder with handlers |
| **Routing** | Conventional based on Controller/Action | Page route-based |
| **Data Binding** | Via Controller (code-behind pattern) | PageModel with @model |
| **Complexity** | Better for complex apps | Better for simple pages |
| **Use Case** | Large applications, APIs | CRUD operations, forms |

**When to use:**
- **MVC:** Large enterprise apps, multiple views per controller
- **Razor Pages:** Single-page forms, CRUD operations

---

### Q5: Exception Handling and REST API Design (5 marks) ⏱️ 13 minutes

#### **a) Exception Handling Code (3 marks)**

```csharp
// Custom Exception
public class InsufficientFundsException : Exception
{
    public InsufficientFundsException(string message) : base(message) { }
}

// Try-Catch-Finally Implementation
public class BankAccount
{
    private decimal balance = 1000;

    public void Withdraw(decimal amount)
    {
        try
        {
            if (amount > balance)
                throw new InsufficientFundsException(
                    $"Cannot withdraw {amount}. Balance: {balance}");
            
            balance -= amount;
            Console.WriteLine($"Withdrawn: {amount}. New Balance: {balance}");
        }
        catch (InsufficientFundsException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Unexpected error: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Transaction attempt completed.");
        }
    }
}

// Usage
var account = new BankAccount();
account.Withdraw(500);   // Success
account.Withdraw(2000);  // Throws custom exception
```

---

#### **b) REST API Endpoints and HTTP Methods (2 marks)**

| HTTP Method | Purpose | ASP.NET Core |
|-------------|---------|---|
| **GET** | Retrieve data | `[HttpGet("{id}")]` |
| **POST** | Create new resource | `[HttpPost]` |
| **PUT** | Update entire resource | `[HttpPut("{id}")]` |
| **DELETE** | Remove resource | `[HttpDelete("{id}")]` |

**Code Example:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet("{id}")]
    public IActionResult GetProduct(int id)
    {
        return Ok(new { id, name = "Laptop" });
    }

    [HttpPost]
    public IActionResult CreateProduct([FromBody] ProductDto dto)
    {
        return Created("", new { id = 1, name = dto.Name });
    }

    [HttpPut("{id}")]
    public IActionResult UpdateProduct(int id, [FromBody] ProductDto dto)
    {
        return Ok(new { id, name = dto.Name });
    }

    [HttpDelete("{id}")]
    public IActionResult DeleteProduct(int id)
    {
        return NoContent();
    }
}
```

---

---

## MODULE 2: COMPLETE ANSWERS (Choose 3 out of 5)

---

### Q1: PWA Concepts and Architecture (5 marks) ⏱️ 12 minutes

#### **a) PWA Definition and Key Characteristics (2 marks)**

**Definition:** Progressive Web Applications (PWAs) are web applications that use modern web technologies to provide app-like experiences directly in the browser.

**Three Key Characteristics:**

1. **Reliable:** Works offline or on slow networks using Service Workers and caching
2. **Fast:** Loads instantly, responsive UI, minimal network requests
3. **Engaging:** Full-screen display, push notifications, home screen installation

---

#### **b) PWA vs Native vs Hybrid Apps (3 marks)**

| Feature | PWA | Native App | Hybrid App |
|---------|-----|-----------|-----------|
| **Platform** | Browser-based | OS-specific | Both |
| **Installation** | Add to home screen | App store | App store |
| **Performance** | Good | Excellent | Moderate |
| **Offline** | Yes (Service Workers) | Yes | Limited |
| **Push Notifications** | Yes | Yes | Yes |
| **Development Cost** | Low | High | Moderate |
| **Updates** | Instant | Manual | Manual |
| **Discoverability** | SEO friendly | App store only | Limited |

**Advantages/Disadvantages:**

**PWA Advantages:** No installation, instant updates, cross-platform  
**PWA Disadvantages:** Limited native features, browser-dependent

**Native Advantages:** Optimal performance, full OS access  
**Native Disadvantages:** High cost, platform-specific development

**Hybrid Advantages:** Code reuse, native + web features  
**Hybrid Disadvantages:** Slower than native, dependency on framework

---

### Q2: Service Workers and Caching Strategies (5 marks) ⏱️ 13 minutes

#### **a) Service Worker Lifecycle (2.5 marks)**

**Lifecycle Stages:**

```
1. REGISTRATION
   ↓
2. INSTALLATION → Install event fires
   ├─ Cache assets (CSS, JS, images)
   ↓
3. ACTIVATION → Activate event fires
   ├─ Clean old caches
   ↓
4. FETCH → Intercept network requests
   ├─ Apply caching strategy
   ├─ Return cached or network response
```

**Code Example:**
```javascript
// Register Service Worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(reg => console.log('SW registered'))
        .catch(err => console.log('SW registration failed'));
}

// sw.js - Service Worker file
const CACHE_NAME = 'v1';
const urlsToCache = ['/', '/styles/style.css', '/script.js'];

// Installation event
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(urlsToCache);
        })
    );
});

// Activation event
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Fetch event
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});
```

---

#### **b) Caching Strategies (2.5 marks)**

**1. Cache First Strategy (Cache, falling back to network):**
```javascript
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) return response;
                return fetch(event.request).then(response => {
                    const cache = caches.open('v1');
                    cache.then(c => c.put(event.request, response.clone()));
                    return response;
                });
            })
    );
});
```
**Use:** Static assets (CSS, JS, images)

**2. Network First Strategy (Network, falling back to cache):**
```javascript
self.addEventListener('fetch', event => {
    event.respondWith(
        fetch(event.request)
            .then(response => {
                const cache = caches.open('v1');
                cache.then(c => c.put(event.request, response.clone()));
                return response;
            })
            .catch(() => caches.match(event.request))
    );
});
```
**Use:** API calls, dynamic content

**3. Stale-While-Revalidate:**
```javascript
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                const fetchPromise = fetch(event.request)
                    .then(response => {
                        caches.open('v1').then(c => c.put(event.request, response));
                        return response;
                    });
                return response || fetchPromise;
            })
    );
});
```
**Use:** Balance between speed and freshness

---

### Q3: Web App Manifest and Offline Functionality (5 marks) ⏱️ 12 minutes

#### **a) Web App Manifest Properties (2.5 marks)**

```json
{
  "name": "My PWA Application",
  "short_name": "MyPWA",
  "description": "A Progressive Web Application",
  "start_url": "/index.html",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#ffffff",
  "theme_color": "#2196F3",
  "icons": [
    {
      "src": "/img/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/img/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

**Essential Properties:**
- **name:** Full application name
- **short_name:** Name on home screen
- **start_url:** Page to load on launch
- **display:** "standalone" (app-like), "fullscreen", "minimal-ui"
- **icons:** App icons for various devices
- **theme_color:** Color for browser UI
- **background_color:** Splash screen color

---

#### **b) Offline Functionality (2.5 marks)**

**Service Workers + Storage Implementation:**

```javascript
// In Service Worker (offline support)
const CACHE_NAME = 'offline-v1';
const offlineURL = '/offline.html';

self.addEventListener('fetch', event => {
    if (event.request.mode === 'navigate') {
        event.respondWith(
            fetch(event.request)
                .catch(() => caches.match(offlineURL))
        );
    }
});

// In main app.js (IndexedDB for data storage)
const db = new Promise(resolve => {
    const request = indexedDB.open('AppDB', 1);
    request.onupgradeneeded = e => {
        e.target.result.createObjectStore('data');
    };
    request.onsuccess = e => resolve(e.target.result);
});

// Save data offline
async function saveData(key, value) {
    const database = await db;
    const tx = database.transaction('data', 'readwrite');
    tx.objectStore('data').put(value, key);
}

// Retrieve data offline
async function getData(key) {
    const database = await db;
    return new Promise(resolve => {
        const request = database.transaction('data').objectStore('data').get(key);
        request.onsuccess = () => resolve(request.result);
    });
}
```

**Practical Example:**
```javascript
// User fills form offline
async function submitFormOffline(formData) {
    try {
        const response = await fetch('/api/submit', {
            method: 'POST',
            body: JSON.stringify(formData)
        });
        return response.json();
    } catch (error) {
        // Save to IndexedDB if offline
        await saveData('pendingForm', formData);
        return { offline: true, message: 'Saved offline' };
    }
}
```

---

### Q4: Responsive Web Design and Security (5 marks) ⏱️ 13 minutes

#### **a) Mobile-First Approach and Media Queries (2 marks)**

**Mobile-First CSS:**
```css
/* Mobile first (base styles for small screens) */
body {
    font-size: 14px;
    padding: 10px;
}

.container {
    width: 100%;
    display: block;
}

.sidebar {
    display: none;
}

/* Tablet (medium screens) */
@media (min-width: 768px) {
    body {
        font-size: 16px;
        padding: 20px;
    }
    
    .container {
        display: flex;
        gap: 20px;
    }
    
    .sidebar {
        display: block;
        width: 25%;
    }
}

/* Desktop (large screens) */
@media (min-width: 1024px) {
    body {
        font-size: 18px;
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

**Benefits:**
- Smaller CSS payload for mobile
- Faster initial load
- Progressive enhancement

---

#### **b) CORS and JWT Authentication (3 marks)**

**CORS in ASP.NET Core:**
```csharp
// Startup.cs / Program.cs
public void ConfigureServices(IServiceCollection services)
{
    services.AddCors(options =>
    {
        options.AddPolicy("AllowPWA", builder =>
        {
            builder.WithOrigins("https://mypwa.com")
                   .AllowAnyMethod()
                   .AllowAnyHeader()
                   .AllowCredentials();
        });
    });
}

public void Configure(IApplicationBuilder app)
{
    app.UseCors("AllowPWA");
}
```

**JWT Authentication Implementation:**

**Backend (C# - Generate Token):**
```csharp
[HttpPost("login")]
public IActionResult Login([FromBody] LoginRequest request)
{
    // Validate credentials
    if (ValidateUser(request.Username, request.Password))
    {
        var claims = new[]
        {
            new Claim(ClaimTypes.NameIdentifier, request.Username),
            new Claim(ClaimTypes.Role, "User")
        };

        var key = new SymmetricSecurityKey(
            Encoding.UTF8.GetBytes("your-secret-key-min-32-chars"));
        var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);
        
        var token = new JwtSecurityToken(
            issuer: "your-app",
            audience: "your-app-users",
            claims: claims,
            expires: DateTime.UtcNow.AddHours(1),
            signingCredentials: creds);

        return Ok(new { token = new JwtSecurityTokenHandler().WriteToken(token) });
    }
    return Unauthorized();
}
```

**Frontend (JavaScript - Use Token):**
```javascript
async function login(username, password) {
    const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    
    const data = await response.json();
    localStorage.setItem('token', data.token);
}

async function fetchProtectedAPI() {
    const token = localStorage.getItem('token');
    const response = await fetch('/api/protected', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    });
    return response.json();
}
```

---

### Q5: PWA Integration and Performance Optimization (5 marks) ⏱️ 13 minutes

#### **a) Consuming ASP.NET Core Web API from PWA (2.5 marks)**

**Step 1: Setup ASP.NET Core API:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class DataController : ControllerBase
{
    [HttpGet]
    public IActionResult GetData()
    {
        var data = new[] {
            new { id = 1, title = "Item 1" },
            new { id = 2, title = "Item 2" }
        };
        return Ok(data);
    }
}
```

**Step 2: PWA Frontend - Fetch API:**
```javascript
// api-client.js
class APIClient {
    constructor(baseURL = '/api') {
        this.baseURL = baseURL;
    }

    async get(endpoint) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });
            
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async post(endpoint, data) {
        const response = await fetch(`${this.baseURL}${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await response.json();
    }
}

// Usage in PWA
const api = new APIClient('/api');
api.get('/data')
   .then(data => console.log(data))
   .catch(error => console.error(error));
```

---

#### **b) Lighthouse Performance Testing (2.5 marks)**

**What is Lighthouse?**
Chrome DevTools integrated auditing tool for performance, accessibility, SEO, best practices.

**How to Use:**
1. Open DevTools (F12)
2. Go to "Lighthouse" tab
3. Select "PWA" category
4. Click "Generate report"

**Three Key Metrics:**

| Metric | Description | Target |
|--------|-----------|--------|
| **First Contentful Paint (FCP)** | Time to display first content | < 1.8s |
| **Largest Contentful Paint (LCP)** | Time to display largest content | < 2.5s |
| **Cumulative Layout Shift (CLS)** | Visual stability (0-1 scale) | < 0.1 |

**Optimization Tips:**
```javascript
// 1. Lazy load images
<img loading="lazy" src="image.jpg">

// 2. Minify CSS/JS
// Use bundler: webpack, parcel

// 3. Enable gzip compression (server config)
// ASP.NET Core:
services.AddResponseCompression();

// 4. Cache resources via Service Worker
// (Already covered in Q2)

// 5. Use CDN for static assets
<link rel="stylesheet" href="https://cdn.example.com/style.css">
```

---

---

## QUICK REFERENCE - TIME ALLOCATION GUIDE

| Module | Questions | Time | Marks |
|--------|-----------|------|-------|
| **Module 1** | Choose 3 of 5 | 32 min | 15 |
| **Module 2** | Choose 3 of 5 | 32 min | 15 |
| **Buffer/Review** | — | -4 min | — |
| **TOTAL** | **6 Qs** | **60 min** | **30** |

---

## TIPS FOR EXAM SUCCESS ✅

1. **Read all questions first** (2 min) - identify easiest 3 per module
2. **Allocate time per question:** ~11-13 minutes per 5-mark question
3. **Write concisely:** Use code snippets, tables, bullet points
4. **Include examples:** Programming questions need working code
5. **Don't elaborate unnecessarily:** Stick to key points
6. **Leave 2-3 minutes for review** at the end

---

**Good Luck! 🚀**

*These answers cover all learning objectives from your syllabus. Study and understand concepts, don't just memorize!*
