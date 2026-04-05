---
created: 2024-06-30
---

## Resolución de errores

### Message: Creation of dynamic property CI_URI::$config is deprecated

I think a better way is to implement #[\AllowDynamicProperties]

Easier and much shorter.

In all the above mentioned classes add #[\AllowDynamicProperties] above class xxxxxx {

I give you my changes:

/system/core/URI.php

```php
#[\AllowDynamicProperties]

class CI_URI {
```

/system/core/Router.php

```php
#[\AllowDynamicProperties]

class CI_Router {
```

/system/core/Loader.php

```php
#[\AllowDynamicProperties]

class CI_Loader {
```

/system/core/Controller.php

```php
#[\AllowDynamicProperties]

class CI_Controller {   
```

/system/database/DB_driver.php

```php
#[\AllowDynamicProperties]

abstract class CI_DB_driver {
```
