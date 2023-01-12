# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-alpha.11 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)


## Public endpoints

* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:37656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (7)
```bash
peers="2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,c28ae12dc190b2abfc578f8ed2fea90fa5ff3b1d@65.108.134.208:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,6c7100291f35132ac1b58ff7c6d05b4ce75512b7@65.108.70.119:36156,372111fd8c3c11a57cd34db58b2bdd8d2b6e5005@172.104.19.93:26656,0e3058446ee9b1ad449b5d3a60d5c4f92dd3785c@65.109.30.12:56656,b26f63f307ca8e80033cbc618f7577e5be7f0c1a@95.217.118.96:27363"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
