# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v0.11.6 | **Wasm**: ON

[Website](https://www.palomachain.com) | [Discord](https://discord.gg/tKVFpfdSw4) | [Twitter](https://twitter.com/paloma_chain)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/paloma](https://explorer.kjnodes.com/paloma)

## Public endpoints

* api: [https://paloma.api.kjnodes.com](https://paloma.api.kjnodes.com)
* rpc: [https://paloma.rpc.kjnodes.com](https://paloma.rpc.kjnodes.com)
* grpc: paloma.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@paloma.rpc.kjnodes.com:11056
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@paloma.rpc.kjnodes.com:11059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/paloma/addrbook.json > $HOME/.paloma/config/addrbook.json
```

**live-peers** (10)
```bash
peers="874ccf9df2e4c678a18a1fb45a1d3bb703f87fa0@65.109.172.249:26656,08c242d4505c5db223647069fdc0acb6e90079aa@65.109.106.214:26656,87b4221770495e66e772a53bbea92a15aff288c2@144.126.158.0:26656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,cb8a1e9e12ac06dbd565311137f6c93d66fd96f8@104.167.221.18:26656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,98b54cd6696e616fe966008ebf2bac409e3e0773@65.108.194.44:26656,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
