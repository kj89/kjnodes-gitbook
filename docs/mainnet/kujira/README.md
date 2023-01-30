# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
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

**live-peers** (10)
```bash
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
