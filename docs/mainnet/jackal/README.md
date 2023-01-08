# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

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

**live-peers** (17)
```bash
peers="e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,ea35106e43dcec1e5c66319272da48df3dce7723@57.128.144.233:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,e61861653d42ebe5d7bf46d4c61f3753091985cd@83.53.221.249:36656,9c149b35243970e1f8e0519f1f33f79f7d5bd91b@51.38.52.188:26638,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,3ebc427c4aea796e7eea5551e8bca74a7734fe52@65.144.145.234:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
