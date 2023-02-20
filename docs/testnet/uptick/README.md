# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.5 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)




## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: [https://uptick-testnet.grpc.kjnodes.com](https://uptick-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (36)
```bash
peers="d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,0afdeea2f014bdfc43ab6dbdf567164daf861cf4@57.128.86.31:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,50e92c60d1b8c6681044778d74caaeef51a26ddd@94.130.207.215:15656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,0fcdc6af694d5b9995340549e5ce444dc96de3e0@195.201.197.4:15656,967e0f06ad8b16dee6a8a6b8a48e8e5a63fdd810@178.211.139.225:7656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,4dfcdb373e4b8d121b89b779e5ca08b957afd884@194.163.180.77:31656,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,c6ca186e2ea0202a78b357c9b2d8883e3d96613a@144.91.110.211:31656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,8096fef589ead4cd3a1aef83110b0241e63d5747@38.242.239.25:26656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,56695e3cbe13a41c03c67670810552d5564a4b30@75.119.130.26:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,75f90b4070eab7a20dc60974c85069389c77d89d@38.242.239.27:26656,d9086eecadb48fa29e0cedcffea0dac7842f82b7@89.252.21.37:26656,60e9b1c88255f3528cf5ad875e99b6b7585fb863@95.217.130.204:15656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,7a9b1f1ed80e854dfbf95f921c35f950f9278ea4@161.97.162.123:31656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,ff4e273818c4f1a0827dbe311162ccf89eb6ee6f@38.242.252.97:15656,bfc2be7e459b947973a15a01055cad86ad34f35c@185.163.127.24:15656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@94.23.23.189:6969,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
