# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,a8f9cedd64e5fb2dc019061985afe8c34fd5efcb@141.94.251.25:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,dd1f96b91053c8d89b1c65d92eebf7ad64c76add@65.21.200.164:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
