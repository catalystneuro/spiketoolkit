from abc import ABC, abstractmethod

# Baseclass for each quality metric

class QualityMetric(ABC):
    def __init__(
        self,
        metric_data,
        metric_name
    ):
        '''
        Parameters
        ----------
        metric_data: MetricData
            An object for storing and computing preprocessed data 
        '''
        self._metric_data = metric_data
        self._metric_name = metric_name

    #implemented by quality metric subclasses
    @abstractmethod
    def compute_metric(self):
        pass

    @abstractmethod
    def threshold_metric(self, threshold, threshold_sign, epoch=0):
        '''
        Parameters
        ----------
        threshold: int or float
            The threshold for the given metric.
        threshold_sign: str
            If 'less', will threshold any metric less than the given threshold.
            If 'less_or_equal', will threshold any metric less than or equal to the given threshold.
            If 'greater', will threshold any metric greater than the given threshold.
            If 'greater_or_equal', will threshold any metric greater than or equal to the given threshold.
        epoch:
            The threshold will be applied to the specified epoch. 
            If epoch is None, then it will default to the first epoch. 
        Returns
        -------
        tc: ThresholdCurator
            The thresholded sorting extractor.
        '''
        pass

    def save_as_property(self, sorting, metric_epochs):
        if len(self._metric_data.get_epochs()) == 1:
            metric = metric_epochs[0]
            for i_u, u in enumerate(sorting.get_unit_ids()):
                sorting.set_unit_property(u, self._metric_name, metric[i_u])
        else:
            raise NotImplementedError(
                "Quality metrics cannot be saved as properties if 'epochs_tuples' are given."
            )