# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.43 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)




## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: [https://nolus-testnet.grpc.kjnodes.com](https://nolus-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```bash
peers="785789b6574c45b8cfefff08344fdfeda345c7e1@135.125.5.34:55666,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,e19fa1dc701b4f0dbbe02ef0ead3b57d2a513429@65.109.169.175:26656,51abbd224cbeaeb6d1a962d07894b356d174e948@38.242.248.112:26656,b1bf9217ad23fd3c7d9c6d65f9ddb7f803b4d542@157.245.63.97:26656,ce6a67a084a25c189ed92522f1a0f6c44ec7cc3a@116.202.227.117:43656,3577f8c3aa36c31b7ef2990e8521698786c8754c@65.21.226.230:29656,e43e3f6c01c94d20a9bbcef5e5eb643090e101c3@65.109.171.22:26656,f0f48327e14e6918a2fad2c795429dd6c3856236@88.99.161.162:43656,c2e461ef97ce664bc1e91ea95ecaa8766f58ce88@65.109.116.110:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
