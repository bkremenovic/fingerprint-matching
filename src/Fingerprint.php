<?php
namespace Bkremenovic\Fingerprint;

use Bkremenovic\Fingerprint\Exceptions\NotInstalledException;
use Bkremenovic\Fingerprint\Exceptions\NotLinuxException;
use Symfony\Component\Process\Process;

use Closure;
use Storage;

class Fingerprint {
    public function __construct() {
        if(strtoupper(PHP_OS) !== "LINUX") {
            throw new NotLinuxException("This package requires Linux, but it appears you are not running it !");
        }

        if(str_contains(exec("type python"), "not found")) {
            throw new NotInstalledException("Python is not installed !");
        }
    }

    public function match($samples, $fingerprint) {
        $process = new Process('python '.__DIR__.'/../match.py --samples="'.addslashes($samples).'" --fingerprint="'.addslashes($fingerprint).'"');
        $process->run();
        $output = trim($process->getOutput());
        
        return $output !== "" ? $output : null;
    }
}
