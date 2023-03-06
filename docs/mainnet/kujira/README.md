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

**live-peers** (17)
```bash
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,9c753f4e99433b79b0b7dce69fffa0a892491f95@65.108.234.154:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
