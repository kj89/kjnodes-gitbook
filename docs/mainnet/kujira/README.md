# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4-mainnet | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: kujira.grpc.kjnodes.com:13090

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

**live-peers** (20)
```bash
peers="9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
