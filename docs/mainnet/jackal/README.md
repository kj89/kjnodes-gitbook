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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:37656,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,ca22db8dc1859e6ebb463317ec44b216e3767d31@185.69.166.158:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,e272f855eb99975dbd23bfc52dce9ff9661596ff@65.109.60.54:37656,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656,5d4e2cd9b6f7a1412cc56509cd6a585272bfe8e4@65.109.65.210:32656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
