# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v2.0.1 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/jackal-testnet](https://explorer.kjnodes.com/jackal-testnet)

## Public endpoints

* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)
* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* grpc: jackal-testnet.grpc.kjnodes.com:13790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:13756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:13759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (11)
```bash
peers="2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,8d99065fe08c2ef79ec4f9f5e97b2a14c9f4853d@202.61.194.254:56656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,dc84774683298e57a848b59b7c0d1a70477b4fc1@213.239.207.175:48656,fd5b3021fe67406e63c1a3e3e89cb243bc0791c9@65.109.32.174:32656,2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,ec78732a7d5bdc1e27e8d7ac1bffe3881c9fb271@65.108.226.183:17556,712dd67b7abe08577d394e90a4930492c8f7d2ee@65.108.124.219:41656,4ea723e652f11433734ae2aa6f364ef0510d6636@16.163.74.176:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
