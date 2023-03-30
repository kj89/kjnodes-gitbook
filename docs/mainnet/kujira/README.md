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

**live-peers** (18)
```bash
peers="ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
