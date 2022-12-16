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
peers="f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
