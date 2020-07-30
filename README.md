# Celery Sample

## Worker

worker only
```bash
$ celery -A celery_sample worker -l info
```

self beat
```bash
$ celery -A celery_sample worker -B -l info
```

## Beat

```bash
$ celery -A celery_sample beat -l info
```

## Ref

https://www.jianshu.com/p/ea86cb9a6bb2