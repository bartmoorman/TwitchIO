from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import twitchio

    from .authentication import UserTokenPayload
    from .models.eventsub_ import SubscriptionRevoked
    from .payloads import TokenRefreshedPayload

async def event_token_refreshed(payload: TokenRefreshedPayload) -> None:
    """Event dispatched when a token managed by the :class:`~twitchio.Client` is successfully refreshed.

    You can use this event to update the stored token locally.

    Parameters
    ----------
    payload: TokenRefreshedPayload
    """

async def event_oauth_authorized(payload: UserTokenPayload) -> None:
    """Event dispatched when a user authorizes your Client-ID via Twitch OAuth on a built-in web adapter.

    The default behaviour of this event is to add the authorized token to the client.
    See: :class:`~twitchio.Client.add_token` for more details.

    Parameters
    ----------
    payload: UserTokenPayload
    """

async def event_subscription_revoked(payload: SubscriptionRevoked) -> None:
    """Event dispatched when Twitch revokes a subscription. This can occur on websockets and webhooks.
    You'll receive this message once and then no longer receive messages for the specified user and subscription type.

    Webhook:
        - The user mentioned in the subscription no longer exists. The notification's status is set to `user_removed`.
        - The user revoked the authorization token or simply changed their password. The notification's status is set to `authorization_revoked`.
        - The callback failed to respond in a timely manner too many times. The notification's status is set to `notification_failures_exceeded`.
        - The subscribed to subscription type and version is no longer supported. The notification's status is set to `version_removed`.

    Websocket:
        - The user mentioned in the subscription no longer exists. The notification's status field is set to `user_removed`.
        - The user revoked the authorization token that the subscription relied on. The notification's status field is set to `authorization_revoked`.
        - The subscribed to subscription type and version is no longer supported. The notification's status field is set to `version_removed`.

    Parameters
    ----------
    payload: SubscriptionRevoked
    """

async def event_ready() -> None:
    """Event dispatched when the Client is ready and has completed login."""

# Eventsub Events

# AutoMod
async def event_automod_message_hold(payload: twitchio.AutomodMessageHold) -> None: ...
async def event_automod_message_update(payload: twitchio.AutomodMessageUpdate) -> None: ...
async def event_automod_settings_update(payload: twitchio.AutomodSettingsUpdate) -> None: ...
async def event_automod_terms_update(payload: twitchio.AutomodTermsUpdate) -> None: ...

# Channel/Broadcaster
async def event_channel_update(payload: twitchio.ChannelUpdate) -> None: ...
async def event_follow(payload: twitchio.ChannelFollow) -> None: ...
async def event_ad_break(payload: twitchio.ChannelAdBreakBegin) -> None: ...
async def event_cheer(payload: twitchio.ChannelCheer) -> None: ...
async def event_raid(payload: twitchio.ChannelRaid) -> None: ...

# Chat/Messages
async def event_message(payload: twitchio.ChatMessage) -> None: ...
async def event_message_whisper(payload: twitchio.Whisper) -> None: ...
async def event_message_delete(payload: twitchio.ChatMessageDelete) -> None: ...
async def event_chat_notification(payload: twitchio.ChatNotification) -> None: ...
async def event_chat_clear(payload: twitchio.ChannelChatClear) -> None: ...
async def event_chat_clear_user(payload: twitchio.ChannelChatClearUserMessages) -> None: ...
async def event_chat_settings_update(payload: twitchio.ChatSettingsUpdate) -> None: ...
async def event_chat_user_message_hold(payload: twitchio.ChatUserMessageHold) -> None: ...
async def event_chat_user_message_update(payload: twitchio.ChatUserMessageUpdate) -> None: ...

# Shared Chat
async def event_shared_chat_begin(payload: twitchio.SharedChatSessionBegin) -> None: ...
async def event_shared_chat_update(payload: twitchio.SharedChatSessionUpdate) -> None: ...
async def event_shared_chat_end(payload: twitchio.SharedChatSessionEnd) -> None: ...

# Subscriptions
async def event_subscription(payload: twitchio.ChannelSubscribe) -> None: ...
async def event_subscription_end(payload: twitchio.ChannelSubscriptionEnd) -> None: ...
async def event_subscription_gift(payload: twitchio.ChannelSubscriptionGift) -> None: ...
async def event_subscription_message(payload: twitchio.ChannelSubscriptionMessage) -> None: ...

# Bans
async def event_ban(payload: twitchio.ChannelBan) -> None: ...
async def event_unban(payload: twitchio.ChannelUnban) -> None: ...
async def event_unban_request(payload: twitchio.ChannelUnbanRequest) -> None: ...
async def event_unban_request_resolve(payload: twitchio.ChannelUnbanRequestResolve) -> None: ...

# Warnings
async def event_warning_acknowledge(payload: twitchio.ChannelWarningAcknowledge) -> None: ...
async def event_warning_send(payload: twitchio.ChannelWarningSend) -> None: ...

# Moderation and VIPs
async def event_mod_action(payload: twitchio.ChannelModerate) -> None: ...
async def event_moderator_add(payload: twitchio.ChannelModeratorAdd) -> None: ...
async def event_moderator_remove(payload: twitchio.ChannelModeratorRemove) -> None: ...
async def event_vip_add(payload: twitchio.ChannelVIPAdd) -> None: ...
async def event_vip_remove(payload: twitchio.ChannelVIPRemove) -> None: ...

# Redemptions and Rewards
async def event_automatic_redemption_add(payload: twitchio.ChannelPointsAutoRedeemAdd) -> None: ...
async def event_custom_reward_add(payload: twitchio.ChannelPointsRewardAdd) -> None: ...
async def event_custom_reward_update(payload: twitchio.ChannelPointsRewardUpdate) -> None: ...
async def event_custom_reward_remove(payload: twitchio.ChannelPointsRewardRemove) -> None: ...
async def event_custom_redemption_add(payload: twitchio.ChannelPointsRedemptionAdd) -> None: ...
async def event_custom_redemption_update(payload: twitchio.ChannelPointsRedemptionUpdate) -> None: ...

# Polls
async def event_poll_begin(payload: twitchio.ChannelPollBegin) -> None: ...
async def event_poll_progress(payload: twitchio.ChannelPollProgress) -> None: ...
async def event_poll_end(payload: twitchio.ChannelPollEnd) -> None: ...

# Predictions

async def event_prediction_begin(payload: twitchio.ChannelPredictionBegin) -> None: ...
async def event_prediction_progress(payload: twitchio.ChannelPredictionProgress) -> None: ...
async def event_prediction_lock(payload: twitchio.ChannelPredictionLock) -> None: ...
async def event_prediction_end(payload: twitchio.ChannelPredictionEnd) -> None: ...

# Suspicious Users
async def event_suspicious_user_message(payload: twitchio.SuspiciousUserMessage) -> None: ...
async def event_suspicious_user_update(payload: twitchio.SuspiciousUserUpdate) -> None: ...

# Charity Campaigns
async def event_charity_campaign_donate(payload: twitchio.CharityCampaignDonation) -> None: ...
async def event_charity_campaign_start(payload: twitchio.CharityCampaignStart) -> None: ...
async def event_charity_campaign_progress(payload: twitchio.CharityCampaignProgress) -> None: ...
async def event_charity_campaign_stop(payload: twitchio.CharityCampaignStop) -> None: ...

# Goals
async def event_goal_begin(payload: twitchio.GoalBegin) -> None: ...
async def event_goal_progress(payload: twitchio.GoalProgress) -> None: ...
async def event_goal_end(payload: twitchio.GoalEnd) -> None: ...

# Hype Train
async def event_hype_train(payload: twitchio.HypeTrainBegin) -> None: ...
async def event_hype_train_progress(payload: twitchio.HypeTrainProgress) -> None: ...
async def event_hype_train_end(payload: twitchio.HypeTrainEnd) -> None: ...

# Shield Mode
async def event_shield_mode_begin(payload: twitchio.ShieldModeBegin) -> None: ...
async def event_shield_mode_end(payload: twitchio.ShieldModeEnd) -> None: ...

# Shoutouts
async def event_shoutout_create(payload: twitchio.ShoutoutCreate) -> None: ...
async def event_shoutout_receive(payload: twitchio.ShoutoutReceive) -> None: ...

# Streams
async def event_stream_online(payload: twitchio.StreamOnline) -> None: ...
async def event_stream_offline(payload: twitchio.StreamOffline) -> None: ...

# OAuth
async def event_user_authorization_grant(payload: twitchio.UserAuthorizationGrant) -> None: ...
async def event_user_authorization_revoke(payload: twitchio.UserAuthorizationRevoke) -> None: ...

# Users
async def event_user_update(payload: twitchio.UserUpdate) -> None: ...
