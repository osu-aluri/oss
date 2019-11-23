import personalBestCache
import userStatsCache
from common.ddog import datadogClient
from common.files import fileBuffer, fileLocks
from common.web import schiavo
from datetime import datetime
try:
	with open("version") as f:
		VERSION = f.read().strip()
except:
	VERSION = "Unknown"
ACHIEVEMENTS_VERSION = 1

DATADOG_PREFIX = "lets"
db = None
redis = None
conf = None
application = None
pool = None
pascoa = {}
starttime = datetime.now()
busyThreads = 0
debug = False
sentry = False

# Cache and objects
fLocks = fileLocks.fileLocks()
userStatsCache = userStatsCache.userStatsCache()
personalBestCache = personalBestCache.personalBestCache()
fileBuffers = fileBuffer.buffersList()
dog = datadogClient.datadogClient()
schiavo = schiavo.schiavo()
achievementClasses = {}