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
peers="79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,e26dd9683b4323a840567356ac12021139d782c1@178.63.52.213:13656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,2e3c72b0b6f3007a109e78864e22661dd7071c06@38.242.130.118:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
