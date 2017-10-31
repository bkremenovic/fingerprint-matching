<?php
	namespace Bkremenovic\Fingerprint\Facades;

	use Illuminate\Support\Facades\Facade;

	class Fingerprint extends Facade {
	    protected static function getFacadeAccessor() {
	        return 'fingerprint';
	    }
	}
