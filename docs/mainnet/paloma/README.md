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
peers="8ed8cddfac504d986a2c6545def0e57b2c6aa5db@65.109.106.172:38656,5321570794c61a8285505812cb7ebd6308a86583@65.109.113.253:26656,527200c42834243b6dc8dacbe26423b7e6577e0f@138.201.129.102:26656,317141e329bc214a76ba92201f6818574ebe5323@135.181.114.98:36656,dfa0d66a3713bf6b49bc509a2a4fc75bee042a30@23.88.77.188:20009,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11056,b3ba407aef9e18e16e8e9a3b523a1b026dabeab3@84.46.248.174:26656,0bcc8119877ba0c701cd230e35c5477da2657bef@5.78.102.204:26656,16f0d09580054101394ea08bbb48b1ad5bb91a27@95.214.52.144:10656,99c890c97afc8abfdfeff662d539af5c504a0baf@88.99.67.234:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.paloma/config/config.toml
```
