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

**live-peers** (19)
```bash
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,6712c72792a0753a4e8d9fae298f50b92892194c@23.175.49.98:10656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
