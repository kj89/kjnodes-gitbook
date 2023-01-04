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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```
peers="ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,2edc8606a894033340ac8e647ff731e437ece150@139.59.8.48:26020,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,2657f7bd2fd2a56ccebeb47f08754ff18e7860c6@176.9.125.13:5060"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
