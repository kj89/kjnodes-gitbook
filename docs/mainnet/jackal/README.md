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

**live-peers** (25)
```bash
peers="753d35e39ad1f6f2fbf0f406a0c4f2bee3c4c7d0@135.181.153.228:56656,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,f1f0efb00b53b50cbee4f53f757bdede9c8c770e@49.12.176.132:22356,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,6e7d2937b3d29952cf83058b81fad4a1ec3b88e8@195.3.223.204:10756,1f7506f1773de3bc12642f5760e016290384a16a@89.58.32.57:37656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
