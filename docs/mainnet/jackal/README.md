# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

Website: [https://jackalprotocol.com](https://jackalprotocol.com)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```
peers="460cf6a14f3fa0f3882400fbdcb80033105cac79@178.154.241.46:26656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,dc579f845ae894cdbe3ab19f1b52387f3d5b681d@23.88.69.167:27211,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
