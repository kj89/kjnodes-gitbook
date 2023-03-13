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

**live-peers** (19)
```bash
peers="9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,1048e73299d435b6598245d246562efc62df002d@65.108.128.201:11856,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,4c22af952c3af002136397d48f9933d0432ace7a@148.251.79.204:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
