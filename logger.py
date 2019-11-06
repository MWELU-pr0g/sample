class Loggeer(object):
	
	def __new__(cls,*args,**kwargs):
	   if not hasattr(cls,'_logger'):

	   	cls._logger=super(logger,cls)__new__(cls,*args,**kwargs)
	   	return cls.logger