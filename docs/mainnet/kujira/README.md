# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

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
peers="263b9b4525e3e568e293677daa0d64d3087815f0@65.108.106.156:26676,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,27227b6c380d806bc9c934bdbd8ca060fb61d7df@217.174.247.59:15602,ccdd8ee4d8fef171e8c2bfaaa2a535033d4af32b@65.108.135.82:29656,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
