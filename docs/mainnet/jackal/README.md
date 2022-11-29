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
peers="68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,433e26fb4d2533d81a2016a7c9ba768dd6ad2177@65.108.194.26:60756,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
