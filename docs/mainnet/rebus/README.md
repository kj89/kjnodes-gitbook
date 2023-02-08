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

**live-peers** (30)
```bash
peers="31dc5c39b845d4e4dedaf1942fbc3afbc2483cf4@65.108.97.58:21656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
