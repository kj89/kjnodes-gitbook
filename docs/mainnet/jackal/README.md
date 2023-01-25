# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

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
peers="399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,460cf6a14f3fa0f3882400fbdcb80033105cac79@178.154.241.46:26656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,d9abd1dd5bf7c57461f0476c61e28bac879430a2@141.94.109.71:10556,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.230:43656,1f7506f1773de3bc12642f5760e016290384a16a@89.58.32.57:37656,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
