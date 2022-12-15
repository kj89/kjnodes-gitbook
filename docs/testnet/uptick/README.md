# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

Website: [https://uptick.network](https://uptick.network)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (23)
```
peers="7175172406a124862dc545b8fb1e3545c35173f9@176.9.146.72:14656,50e92c60d1b8c6681044778d74caaeef51a26ddd@94.130.207.215:15656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,79888e0547bfb9937e4a6f4fbdca7ccbf46cbbde@155.133.23.88:26656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,12fe5ed38770b4bb59c59e183ec1161aebda2a4e@185.173.38.18:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,821cec653e1bdcd6e0ea7db62ddc65e7dae9fc5b@190.2.136.58:26656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,2d892493335b4bb1582dabcaa1e832bcba041e79@95.217.4.62:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
