# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (18)
```bash
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,505ddf90cacbcef8c1acc5e0eacbdd276a269588@195.3.222.240:26356,a0927acbf1e931fc16e11e454b328c991e56d3fe@51.89.155.17:44656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
