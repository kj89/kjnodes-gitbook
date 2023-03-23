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
peers="0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.216.235.54:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@95.217.65.54:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,7c26c34148779b1d0979eb069dbe354752a3644f@5.9.84.213:25656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,6212f700687500f96ef56af3488e99fc4b009e19@212.68.34.95:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
