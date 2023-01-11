# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

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

**live-peers** (10)
```bash
peers="fc593f5f9fcf7f88790bd8274ebc791f612d3efe@65.21.89.54:26655,0179a6055fc1e36053facef08766d06186f3cd33@65.21.200.224:11856,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,bd1ec9985e9f3a1fbfbd7be5fa4c926a61cbd403@34.70.228.207:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,35af92154fdb2ac19f3f010c26cca9e5c175d054@65.108.238.61:27656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
