# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/jackal](https://explorer.kjnodes.com/jackal)

## Public endpoints

* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)
* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* grpc: [https://jackal.grpc.kjnodes.com](https://jackal.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (20)
```bash
peers="ecb163fca7436befa3a5694a7d558e89d3f04b2c@65.109.29.150:17656,4118b172fc2a45e0335c59641fd7c2e5e5e2c53c@65.108.238.203:28656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656,271625e66eed066b35e8e7c84a0bf62c3b0429eb@155.133.22.8:23856,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,753d35e39ad1f6f2fbf0f406a0c4f2bee3c4c7d0@135.181.153.228:56656,9c149b35243970e1f8e0519f1f33f79f7d5bd91b@51.38.52.188:26638,140e8811d3245e12e42b0b99a68f4b5b900823d3@62.210.91.3:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
