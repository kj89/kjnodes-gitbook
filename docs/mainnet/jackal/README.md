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
peers="637166728d6103ad4ec9fff97a321a024bff3e58@65.109.94.221:28656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,460cf6a14f3fa0f3882400fbdcb80033105cac79@178.154.241.46:26656,ef8c470a03f3753df53dad15a435f99d6869f6a7@51.81.107.95:10856"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
