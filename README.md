# Laravel / Lumen fingerprint matching for SecuGen Hamster Plus
Laravel / Lumen package that allows you to match fingerprints scanned with SecuGen Hamster Plus device (using minutiae templates)

#### Include a package into your project using composer:
```
composer require bkremenovic/fingerprint-matching dev-master
```

#### Install dependencies:
```
sudo apt install python
sh vendor/bkremenovic/fingerprint-matching/install.sh
```

#### Open your config/app.php and add the following to the providers array:
```
Bkremenovic\Fingerprint\FingerprintServiceProvider::class,
```

#### In the same config/app.php and add the following to the aliases array: 
```
'Fingerprint' => Bkremenovic\Fingerprint\Facades\Fingerprint::class,
```

# Usage
Use ```match()``` method using a fingerprint to match as a first parameter, and fingerprint samples folder as a second parameter.
If the fingerprint has been successfully matched, it will return a string containing filename of the matching sample. Otherwise, it will return null.

#### Example:

```
Fingerprint::match("fingerprints/samples/", "/tmp/filebkdEfX");
```
Or match with an uploaded file
```
Fingerprint::match("fingerprints/samples/", $request->file('fingerprint'));
```
