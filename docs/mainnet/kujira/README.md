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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656,e81c56107cc4506c1d6645cbe64f115beaccef26@34.69.24.60:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,3a15fa46fe0a27d4ee60497a470a8c91911a9e5e@15.235.66.89:11756,09076c7908db88316498cf4cd4702a8d269e0da9@15.235.114.85:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
