# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: rebus.grpc.kjnodes.com:21090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (21)
```bash
peers="10eb2d456219ea712c696251ddf231bbec6d987c@65.109.37.58:15656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,bd5a6419c073d6cb97bddcfcfd2059bdec41e6a8@185.144.99.33:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
