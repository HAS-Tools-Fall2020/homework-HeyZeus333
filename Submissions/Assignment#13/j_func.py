# %%


def prediction(wk, lastweek, lastweekx2, lastweekx3,
               precip, temp, temp2, intercept_, coef_, weeklypred):
    '''Function (prediction):
    This function that makes a prediction that is a specified length.
    The data utilizes a 6 times dependent linear regressive model.
    Parameters
    ----------
    wk: list
            How many timesteps you want the model to run for.
    lastweek: list (three parameters)
            Flow values for the last three weeks before model starts.
    precip: list
            is predicted rainfall that is length wk.
    temp: list (two parameters)
            Expected temperatures for the duration of the model
    intercept_: int
            The intercept of the model.
    coef_: list
            Coeficeints of the model (slope).
    Returns
    ------
    Weeklypred: list
            Is where you want the prediction data to be stored.
    '''
    for i in range(wk):
        # appends to last week so that they refer to next time step
        lastweekx2.append(lastweek[i])
        lastweekx3.append(lastweekx2[i])

        # temp of second week is number appended
        temp2.append(temp[i])
        # the prediction for week # i
        prediction = intercept_ + coef_[0] * lastweek[i] + coef_[1] \
            * lastweekx2[i] + coef_[2] * lastweekx3[i] + coef_[3] * precip[i] \
            + coef_[4] * temp[i] + coef_[5] * temp2[i]
        lastweek.append(prediction)

        # creates a list of just my predictions for week 1 then week 2
        weeklypred.append(prediction)

    # prints the prediction that you will use
    print(f'The prediction for week 1 is {str(weeklypred[0].round(2))} cfs '
          f'and week 2 is {str(weeklypred[1].round(2))} cfs')


# %%
def pred_sem(lastweek, lastweekx2, lastweekx3, P, temp,
             temp2, intercept_, coef_, weeklypred):
    '''Function (prediction):
    This function that makes a prediction that is a specified length.
    The data utilizes a 6 times dependent linear regressive model.
    Has a probability distribution portion but is 0 by default
    Parameters
    ----------
    wk: list
            How many timesteps you want the model to run for.
    lastweek: list (three parameters)
            Flow values for the last three weeks before model starts.
    monthly_precip: list
            Is predicted rainfall that is length wk.
    temp: list (two parameters)
            Expected temperatures for the duration of the model
    intercept_: int
            The intercept of the model.
    coef_: list
            Coeficeints of the model (slope).
    flow_weekly: dataframe
            A dataframe where flow observed flow comes from
            by default starts at the week of 8/21/20
    Returns
    ------
    Weeklypred: list
            Is where you want the prediction data to be stored. Along,
            with a graph of observed flow and predicted flow
    '''
    for i in range(16):
        # appends to last week so that they refer to next time step
        lastweekx2.append(lastweek[i])
        lastweekx3.append(lastweekx2[i])
        P.append(0)
        # the prediction for week # i
        prediction = intercept_ + coef_[0] * lastweek[i] + coef_[1] \
            * lastweekx2[i] + coef_[2] * lastweekx3[i] + coef_[3] * P[i] \
            + coef_[4] * temp[i] + coef_[5] * temp2[i]
        lastweek.append(prediction)

        # creates a list of just my predictions for week 1 then week 2
        weeklypred.append(prediction)
