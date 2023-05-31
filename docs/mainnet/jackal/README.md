# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v2.0.1 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/jackal](https://explorer.kjnodes.com/jackal)

## Public endpoints

* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)
* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* grpc: jackal.grpc.kjnodes.com:13790

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:13756
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:13759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```bash
peers="0daa5dcda773b1d3842ba2881cf27aab519a2cac@54.36.108.222:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13756,f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,11aeebfb549832b53d58c01a5b15e72746f2b4ce@15.235.87.236:26656,ac8b52dd329a11d2351e264b6ee19808c2bfa22b@75.119.139.114:26656,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,51cbeb39315ef7366b77953ebf6ad905443e6e30@65.109.93.44:17556,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,b15c8d32e2ab76a21434a8e0cb1b94ca63e7da8a@85.239.241.71:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
