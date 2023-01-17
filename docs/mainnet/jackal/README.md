# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
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

**live-peers** (22)
```bash
peers="fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,4118b172fc2a45e0335c59641fd7c2e5e5e2c53c@65.108.238.203:28656,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,cebe2ad7290ce193069a938910905518a37f40c0@35.242.212.157:26656,aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
