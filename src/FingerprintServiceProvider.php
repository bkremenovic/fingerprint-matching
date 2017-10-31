<?php
    namespace Bkremenovic\Fingerprint;

    use Illuminate\Support\ServiceProvider;

    class FingerprintServiceProvider extends ServiceProvider {
        public function register() {
            $this->app->bind('fingerprint', 'Bkremenovic\Fingerprint\Fingerprint');
        }
    }