# Celery Sample

## Worker

worker only
```bash
$ celery -A celery_sample worker -l info
```

celery hostname

```bash
$ celery -A celery_sample worker -l info -n celery-worker-2
```

```bash
$ celery -A celery_sample worker -l info --hostname=celery-worker-2
```


self beat
```bash
$ celery -A celery_sample worker -B -l info
```

## Beat

```bash
$ celery -A celery_sample beat -l info
```

## Flower

```bash
$ celery -A celery_sample flower
```

## Ref

https://www.jianshu.com/p/ea86cb9a6bb2