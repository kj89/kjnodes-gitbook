# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/paloma.png" alt=""><figcaption></figcaption></figure>

Paloma is a fast, permissionless, Cosmos-SDK blockchain that  moves messages securely, between any other blockchains.

**Chain ID**: messenger | **Latest Version Tag**: v1.1.0 | **Wasm**: ON

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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056,1a0232b9426aa1c7a78c92a2136b69d050bb6942@65.108.224.126:26656,e833844c00b8ce60ce6826f170becfa18e6172c2@46.4.27.59:26656,527200c42834243b6dc8dacbe26423b7e6577e0f@138.201.129.102:26656,8af8dfa817359036f55f6793b0ed4bcce8884027@85.14.245.70:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,0c5156a1b644d05c0601063e55984a1909321e29@144.76.97.251:45656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,e5bee82a116c174abf0981c20c34d0e13a7f6c1d@81.0.221.57:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
