# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

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

**live-peers** (28)
```bash
peers="b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
