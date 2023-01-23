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
peers="83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,d00e181b66ce25775ddf5e112ebb6ff587654833@65.144.145.234:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@176.42.25.134:26656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
